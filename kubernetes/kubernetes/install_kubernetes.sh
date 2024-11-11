#!/bin/bash
# Detect the primary network interface
PRIMARY_IFACE=$(ip -br link show | awk '{if ($2 == "UP") {print $1; exit}}')
if [ -z "$PRIMARY_IFACE" ]; then
    echo "No active network interface found."
    exit 1
fi
# Get the IP address from the detected interface
MASTER_IP=$(ip addr show "$PRIMARY_IFACE" | awk '/inet / {print $2}' | cut -d/ -f1)

if [ -z "$MASTER_IP" ]; then
    echo "Unable to detect IP address for interface $PRIMARY_IFACE."
    exit 1
fi

echo "Detected master IP: $MASTER_IP"
# Variables

#MASTER_IP="192.168.1.2"
POD_NETWORK_CIDR="10.10.0.0/16"
KUBEADM_TOKEN="7ohiq0.vtkz1vgz3qw1726j"
DISCOVERY_TOKEN_CA_CERT_HASH="sha256:af0c545b56b87bdb0bdb040cccf55dfb8da1d2ea27f4c38c90e22a98b49a89c8"
CRI_SOCKET="unix:///var/run/containerd/containerd.sock" # Change if using CRI-O

# Function to install Kubernetes components
install_kubernetes() {
    sudo apt update
    sudo apt install -y curl ca-certificates apt-transport-https

    echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.28/deb/ /" | sudo tee /etc/apt/sources.list.d/kubernetes.list
    curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
    sudo apt update
    sudo apt install -y kubelet kubectl kubeadm
}

# Function to configure containerd
configure_containerd() {
    sudo mkdir -p /etc/containerd
    sudo sh -c "containerd config default > /etc/containerd/config.toml"
    sudo sed -i 's/ SystemdCgroup = false/ SystemdCgroup = true/' /etc/containerd/config.toml
    sudo systemctl restart containerd.service
}

# Function to configure sysctl and modules
configure_sysctl_modules() {
    cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

    sudo modprobe overlay
    sudo modprobe br_netfilter

    cat << EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward = 1
EOF

    sudo sysctl --system
}

# Function to initialize master node
initialize_master() {
    sudo kubeadm config images pull
    sudo kubeadm init --pod-network-cidr=$POD_NETWORK_CIDR --apiserver-advertise-address=$MASTER_IP
    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config

    kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/tigera-operator.yaml
    curl https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/custom-resources.yaml -O
    sed -i "s/cidr: 192\.168\.0\.0\/16/cidr: $POD_NETWORK_CIDR/g" custom-resources.yaml
    kubectl create -f custom-resources.yaml
}

# Function to join worker node to master
join_worker() {
    sudo kubeadm join $MASTER_IP:6443 --token $KUBEADM_TOKEN --discovery-token-ca-cert-hash $DISCOVERY_TOKEN_CA_CERT_HASH --cri-socket $CRI_SOCKET
}

# Main script
echo "Are you installing on a master or worker node? (Enter 'master' or 'worker')"
read NODE_TYPE

if [ "$NODE_TYPE" == "master" ]; then
    install_kubernetes
    configure_containerd
    configure_sysctl_modules
    initialize_master
elif [ "$NODE_TYPE" == "worker" ]; then
    install_kubernetes
    configure_containerd
    configure_sysctl_modules
    join_worker
else
    echo "Invalid input. Please enter 'master' or 'worker'."
    exit 1
fi
