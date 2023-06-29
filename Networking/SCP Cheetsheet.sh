#Basic SCP Cheetsheet

scp source_file_path destination_file_path

#uploading

#single file

scp ~/my_local_file.sh user@remote_host_ip:/destination/remote/directory

#Multiple file uploding

scp test.txt test1.txt username@remote_host_ip:/destination/remote/directory


##Downloding

#single file

scp user@remote_host_ip:/destination/remote/directory ~/local_file.txt

#multiple file

scp username@remote_host_ip:/destination/remote/directory/\{test.sh,test1.sh\} .

#verbose output

scp -v source_filep_path destination_file_path