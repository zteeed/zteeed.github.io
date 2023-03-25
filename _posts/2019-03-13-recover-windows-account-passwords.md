---
title: EN - Recover Windows account passwords
---

> This article might help you to retrieve plaintext passwords from Windows
> sessions. I disclaim any liability if you use this article for illegal actions.
> If you want to train, you can downloads some virtual machines below, this
> tutorial is also made for you if you are working on a real Windows Operating
> System.

# Step 0: Download the virtual machines (training mode)

> If you are working on a real Windows operating system, just skip this until Step
> 1.

### Main source

<ul>
<li><a
href="https://windaube.hackademint.org/Windaube1.ova">Windaube1.ova </a>(sha1sum: 5c6d1267a7090a1a9ee2158fce8616d6014ce306)</li>
<li><a
href="https://windaube.hackademint.org/Windaube2.ova">Windaube2.ova</a> (sha1sum: 1583b98694d849f72b8695b0934f49c3db6218fd)</li>
</ul>

### Alternative source

<ul>
<li><a
href="https://windaube.minet.net/Windaube1.ova">Windaube1.ova </a>(sha1sum: 5c6d1267a7090a1a9ee2158fce8616d6014ce306)</li>
<li><a
href="https://windaube.minet.net/Windaube2.ova">Windaube2.ova</a> (sha1sum: 1583b98694d849f72b8695b0934f49c3db6218fd)</li>
</ul>

### Upload the virtual machines

Uplaod the `ova`'s files into [VirtualBox](https://www.virtualbox.org/).

# Step 1: Boot on a Linux Live OS

## Step 1.1: Download a live iso

You can download [here](https://www.kali.org/downloads/) the iso file of 
`Kali Linux 64 Bit` or `Kali Linux 32 Bit`, depending on your CPU computer. 
If you do not know, try first with `Kali Linux 32 Bit`

<img class="img_posts" src="/images/posts/WindowsHacking/Windaube1/kali_download.png">

##  Step 1.2: Making a bootable usb key from iso

> Skip this step if you are working on the virtual machines until Step 1.3

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


## Step 1.3: Boot on a live linux operating system

> Skip this step if you are working on a real Windows Operating System until Step 1.4.

<ul>

<li>Add the ISO to the configuration of the virtual machine
<img class="img_posts" src="/images/posts/WindowsHacking/Windaube1/live_kali_vbox.png">
</li>

</ul>

## Step 1.4: Boot on the live linux operating system (kali)

<ul>

<li>Start the virtual machine and select `Live (amd64)`
<img class="img_posts" src="/images/posts/WindowsHacking/Windaube1/kali_boot_live.PNG">
</li>

</ul>

# Step 2: Get an admin user from scratch

> If you already get an admin account, go to Step 3.2

## Step 2.1: If you DO NOT get a user on the Windows system 

> If you already have an unpriviledge account, go to Step 2.2.

<ul>
<li>Mount the Windows partition with read/write option and replace Utilman.exe
(Utility Manager application of Windows) by cmd.exe in order to get an 
administrator shell without need to authenticate. In my case, `/dev/sda2` is the
Windows partition.
<img class="img_posts" src="/images/posts/WindowsHacking/Windaube2/utilman_to_cmd.PNG">
</li>
</ul>

## Step 2.2: If you already get a user on the Windows system 

<ul>
<li>Mount the Windows partition with read/write option and promote your existing
user as an administrator using `chntpw` command. `windaube` is the unpriviledge
user that already exist on my Windows, replace it by yours when using `chntpw -u
&lt;user&gt; Windows/System32/config/SAM`.
<img class="img_posts" src="/images/posts/WindowsHacking/Windaube1/kali_live_chntpw_start.PNG">
<img class="img_posts" src="/images/posts/WindowsHacking/Windaube1/kali_live_chntpw_user.PNG">
<img class="img_posts" src="/images/posts/WindowsHacking/Windaube1/kali_live_chntpw_promote.PNG">
<img class="img_posts" src="/images/posts/WindowsHacking/Windaube1/kali_live_chntpw_promote_write.PNG">

</li>
</ul>

# Step 3: Retrieve passwords hash of administrators users

## Step 3.1: If you DO NOT get a user on the Windows system 

> Skip this step to Step 3.2 if you already have your access to an administrator
> user on the Windows system.

<ul>

<li>Click on the Utility Manager application of Windows from the administrator
login interface in order to trigger an administrator Windows shell, then create
a new account. If you get an error on `net localgroup Administrateurs hacker_user
/add`, your user if created but is not an administrator so go back to Step 2.1
in order to promote your new user as an administrator. `Administrateurs` is the
name for the localgroup for administrators on my french Windows install (in
English it might be `administrators` or `Administrators`)
<img class="img_posts" src="/images/posts/WindowsHacking/Windaube2/utilman.png">
<img class="img_posts" src="/images/posts/WindowsHacking/Windaube2/create_user.PNG">
</li>

<li>So we created a new user `hacker_user` with password=`password`, let's login
<img class="img_posts" src="/images/posts/WindowsHacking/Windaube2/new_user.PNG">
</li>

</ul>

## Step 3.2: Download mimikatz

<ul>

<li>Mimikatz is a power tool made by `gentilkiwi` that
will enable us to get the passwords hash of all users on the system. If you
asked why do we need an administrator account to use this tool, its because you
need the administrator privilege to disable Windows Defender that is blocking
the downlaod of this tool.
<img class="img_posts" src="/images/posts/WindowsHacking/Windaube1/windows_defender_disable.PNG">
<img class="img_posts" src="/images/posts/WindowsHacking/Windaube1/mimikatz_download.PNG">
<img class="img_posts" src="/images/posts/WindowsHacking/Windaube1/mimikatz_keep.PNG">
<img class="img_posts" src="/images/posts/WindowsHacking/Windaube1/mimikatz_exec_admin.PNG">
<img class="img_posts" src="/images/posts/WindowsHacking/Windaube1/mimikatz_dump1.PNG">
<img class="img_posts" src="/images/posts/WindowsHacking/Windaube1/mimikatz_dump2.PNG">
</li>

<li>
Same thing with the other virtual machine:
<img class="img_posts" src="/images/posts/WindowsHacking/Windaube2/mimikatz_dump2.PNG">
</li>

</ul>

# Step4: From hash to plaintext (passcracking)

#### With the two virtual machines we get several hashes we are going to break.

Write this into a file called `hashes.txt`:
```
windaube:a8bc9746281c76995222af521a5a02d7
hacker_user:8846f7eaee8fb117ad06bdd830b7586c
HackademINT-Windaube1:a779a6cb2541da6cacc4f2c55d1e6c66
HackademINT-Windaube2:458fccb8bf74b63b6ab6e54347f005cf
```

## Step 4.1: Using an online tool

Go to [this website](https://crackstation.net/) and let's see what happened. If
the passwords are not strong enought, it would be easy to get the plaintext
password from the hash using online tools

## Step 4.2: Using hashcat

[Hashcat](https://hashcat.net/hashcat/) is the world's fastest password cracker
tool. In this tutorial, the passwords of administrator looks like
`Windaube{this_is_the_password_content}`, so we need to do a rule-based attack.

Write into a file called rule.txt: `$} ^{ ^e ^b ^u ^a ^d ^n ^i ^W`

Do not forget to download a good wordlist in order to bruteforce passwords, you
can use [rockyou.txt](https://www.scrapmaker.com/data/wordlists/dictionaries/rockyou.txt)

Try to break the hashes with and without the custom rule !

```bash
hashcat -a 0 -m 1000 hashes.txt rockyou.txt --user -O
hashcat -a 0 -m 1000 hashes.txt rockyou.txt -r rule.txt --user -O
```

When it is finished, show the result with:

```bash
hashcat -m 1000 hashes.txt --user --show

hacker_user:8846f7eaee8fb117ad06bdd830b7586c:password
HackademINT-Windaube2:458fccb8bf74b63b6ab6e54347f005cf:Windaube{yuszyuszyusz}
HackademINT-Windaube1:a779a6cb2541da6cacc4f2c55d1e6c66:Windaube{intoxicating}
windaube:a8bc9746281c76995222af521a5a02d7:windaube
```
