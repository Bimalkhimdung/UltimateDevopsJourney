import os
import shutil
import subprocess
from datetime import datetime

def get_dir_size(path):
    """ Calculate the total size of a directory and it's content in bytes,
    more aligned with how 'du' calculates it """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        # Add size of directory itself (metadata)
        try:
            total_size += os.path.getsize(dirpath)
        except (OSError, FileNotFoundError):
            pass
            
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                # Round up to the nearest block size (usually 4KB)
                file_size = os.path.getsize(fp)
                block_size = 4096  # Standard block size on many systems
                if file_size % block_size:
                    file_size = ((file_size // block_size) + 1) * block_size
                total_size += file_size
            except (OSError, FileNotFoundError, PermissionError):
                pass
    return total_size

def get_disk_usage(path):
    try:
        total, used, free = shutil.disk_usage(path)
        return{
            'total': total,
            'used': used,
            'free': free,
            'used_percent': (used/total) * 100
        }
    except Exception as e:
        return f"Error while getting disk usage, {e}"
    
def format_size(size_byte):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_byte < 1024.0:
            return f"{size_byte:.2f} {unit}"
        size_byte = size_byte/1024.0
    return f"{size_byte:.2f} PB"

def monitor_directory(directory_path):
    if not os.path.exists(directory_path):
        return f"Directory {directory_path} does not exist."
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    dir_size_bytes = get_dir_size(directory_path)
    dir_size_formatted = format_size(dir_size_bytes)
    
    disk_usage = get_disk_usage(directory_path)
    
    report = f"Storage Report - {timestamp}\n"
    report += f"Directory: {directory_path}\n"
    report += f"Size: {dir_size_formatted}\n"
    
    if isinstance(disk_usage, dict):
        report += f"Disk Total: {format_size(disk_usage['total'])}\n"
        report += f"Disk Used: {format_size(disk_usage['used'])} ({disk_usage['used_percent']:.2f}%)\n"
        report += f"Disk Free: {format_size(disk_usage['free'])}\n"
    else:
        report += f"{disk_usage}\n"
    
    return report


if __name__ == "__main__":
    import sys
    
    # Check if a directory was specified as a command-line argument
    directory_to_check = "/home/bimal"  # Default
    if len(sys.argv) > 1:
        directory_to_check = sys.argv[1]
    
    # Check if running as root, if not, restart with sudo
    if os.geteuid() != 0:
        print("Script needs to run with sudo privileges to access all files.")
        print("Restarting with sudo...")
        args = ['sudo', 'python3', __file__]
        if len(sys.argv) > 1:
            args.append(sys.argv[1])
        subprocess.run(args)
    else:
        report = monitor_directory(directory_to_check)
        print(report)