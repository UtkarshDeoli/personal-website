
+++
title = 'Install Arch Guide'
date = 2024-04-15T07:48:17+05:30
draft = false
+++

# How to Install Arch Linux

## Step 1: Download the Arch Linux ISO

- Go to the [Arch Linux website](https://archlinux.org/) and navigate to the download section.
- Download the latest Arch Linux ISO image.

## Step 2: Create Bootable Media

- Use a USB drive or a CD/DVD to create a bootable installation media.
- You can use tools like Rufus, Etcher, or dd command on Linux to write the ISO image to the media.

## Step 3: Boot into Arch Linux Live Environment

- Insert the bootable media into your computer and boot from it.
- You will be greeted with the Arch Linux boot menu.

## Step 4: Set the Keyboard Layout

- Use the `loadkeys` command to set your keyboard layout if necessary.
- For example, for a US keyboard layout, you would use `loadkeys us`.

## Step 5: Connect to the Internet

- Use the `ip link` command to identify your network interface.
- Use `ip link set <interface> up` to bring up the interface.
- Use `wifi-menu` to connect to a Wi-Fi network, or `dhcpcd` to obtain an IP address via DHCP for a wired connection.

## Step 6: Partition the Disk

- Use tools like `fdisk`, `parted`, or `cfdisk` to partition your disk.
- Create at least one partition for the root filesystem (e.g., `/dev/sda1`).

## Step 7: Format the Partitions

- Format the partitions using appropriate filesystems.
- For example, use `mkfs.ext4 /dev/sda1` to format a partition with the ext4 filesystem.

## Step 8: Mount the Partitions

- Mount the root partition to `/mnt`.
- For example, `mount /dev/sda1 /mnt`.

## Step 9: Install the Base System

- Use the `pacstrap` command to install the base system packages.
- For example, `pacstrap /mnt base linux linux-firmware`.

## Step 10: Generate an fstab File

- Generate an fstab file to define how disk partitions should be mounted.
- Use `genfstab -U /mnt >> /mnt/etc/fstab`.

## Step 11: Chroot into the Installed System

- Use `arch-chroot` to change the root into the installed system.
- For example, `arch-chroot /mnt`.

## Step 12: Set the Time Zone

- Set the correct time zone using the `ln` command.
- For example, `ln -sf /usr/share/zoneinfo/Region/City /etc/localtime`.

## Step 13: Generate Localization Settings

- Uncomment desired locales in `/etc/locale.gen`.
- Generate the locales with `locale-gen`.
- Set the system language with `echo LANG=en_US.UTF-8 > /etc/locale.conf`.

## Step 14: Set Hostname

- Set the hostname of your system with `echo myhostname > /etc/hostname`.

## Step 15: Set Root Password

- Set the root password with the `passwd` command.

## Step 16: Install a Boot Loader

- Install a boot loader like GRUB or systemd-boot.
- For GRUB, install it with `pacman -S grub` and then run `grub-install --target=i386-pc /dev/sdX` (replace `/dev/sdX` with your disk).
- Generate the GRUB configuration file with `grub-mkconfig -o /boot/grub/grub.cfg`.

## Step 17: Reboot

- Exit the chroot environment by typing `exit`.
- Unmount all mounted partitions with `umount -R /mnt`.
- Reboot your system with `reboot`.
