How to create ssh-key:
1) open Terminal
2) enter 
    ssh-keygen -t ed25519 -C "mregorova@mail.ru"
    ssh-add .ssh/id_ed25519
    ssh-add -l
    ssh -T git@github.com
3) now enter your SSH to git window
4) hurray!
