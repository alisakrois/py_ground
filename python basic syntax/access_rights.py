"""
The virus attacked the filesystem of the supercomputer and broke the control of access rights to the files.
For each file there is a known set of operations which may be applied to it:
    write W,
    read R,
    execute X.
The first line contains the number N — the number of files contained in the filesystem.
The following N lines contain the file names and allowed operations with them, separated by spaces.
The next line contains an integer M — the number of operations to the files. In the last M lines specify the operations
that are requested for files. One file can be requested many times.

You need to recover the control over the access rights to the files.
For each request your program should return OK if the requested operation is valid
or Access denied if the operation is invalid.
"""

access = {}
move = {'read': 'R', 'write': 'W', 'execute': 'X'}
for _ in range(int(input())):
    name_file, *access_file = input().split()
    access[name_file] = access_file

for _ in range(int(input())):
    ac_1, file = input().split()
    if move[ac_1] not in access[file]:
        print('Access denied')
    else:
        print('OK')