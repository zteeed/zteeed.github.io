---
title: Windows Hacking 
published: true
---

> This article might help you to retrieve plaintext passwords from Windows
> sessions. I disclaim any liability if you use this article for illegal actions.
> If you want to train with Windows virtual machines, here is a training
> tutorial: [tutorial](/Windows-Hacking-Training)

# Step1: Boot on a Linux Live OS

## Download a live iso

You can download [here](https://www.kali.org/downloads/) the iso file of 
`Kali Linux 64 Bit` or `Kali Linux 32 Bit`, depending on your CPU computer. 
If you do not know, try first with `Kali Linux 32 Bit`

## Making a bootable usb key from iso

### On Windows

Install [Rufus](https://rufus.ie/) and follow the instructions

![](https://rufus.ie/pics/rufus_en.png)

### On Linux

> Be sure of what you are doing, you is going to delete your device data where
> /dev/sdX is your device, to print device list, use `lsblk` command

```bash
sudo dd if=my_iso_file.iso of=/dev/sdX bs=4M status=progress
```

### Further information

If you want to boot from your USB key, you might need to disable `Secure Boot`
in your BIOS options. To show booting option, you need to spam `F12` on startup.

# Step2: Follow the tutorial

Follow [this tutorial](/Windows-Hacking-Training) skipping the step 0.
