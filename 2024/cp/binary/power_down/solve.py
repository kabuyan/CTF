cmp = [0x00000009, 0x0000000e, 0x00000009, 0x00000001, 0x00000009, 0x0000000e, 0x0000000a, 0x00000010,
       0x00000009, 0x0000000b, 0x0000000c, 0x00000015, 0x00000007, 0x00000000, 0x0000000b, 0x0000000b,
       0x00000008, 0x0000000b, 0x0000000a, 0x0000000f, 0x0000000b, 0x00000013, 0x00000009, 0x0000000b,
       0x0000000b, 0x00000010, 0x0000000a, 0x00000001, 0x00000009, 0x00000008, 0x00000008, 0x0000000d,
       0x00000009, 0x00000003, 0x0000000b, 0x00000005, 0x0000000a, 0x00000005, 0x00000008, 0x0000000c,
       0x0000000a, 0x00000005, 0x0000000b, 0x00000006, 0x00000009, 0x00000000, 0x0000000b, 0x00000004,
       0x00000009, 0x00000010, 0x0000000a, 0x00000012, 0x0000000b, 0x00000014, 0x00000006, 0x00000003,
       0x0000000c, 0x00000013, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000]

print("".join([chr(cmp[i]**2-cmp[i+1]) for i in range(0, len(cmp), 2)]))
