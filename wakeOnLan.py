import usocket
import time
import secrets

broadcast = usocket.socket(usocket.AF_INET, usocket.SOCK_DGRAM)
sendhere = (secrets.BROADCAST, 9)
data = bytearray(102)
data[0] = data[1] = data[2] = data[3] = data[4] = data[5] = 0xff
data[6] = data[12] = data[18] = data[24] = data[30] = data[36] = data[42] = data[48] = data[54] = data[60] = data[66] = data[72] = data[78] = data[84] = data[90] = data[96] = secrets.MAC[0]
data[7] = data[13] = data[19] = data[25] = data[31] = data[37] = data[43] = data[49] = data[55] = data[61] = data[67] = data[73] = data[79] = data[85] = data[91] = data[97] = secrets.MAC[1]
data[8] = data[14] = data[20] = data[26] = data[32] = data[38] = data[44] = data[50] = data[56] = data[62] = data[68] = data[74] = data[80] = data[86] = data[92] = data[98] = secrets.MAC[2]
data[9] = data[15] = data[21] = data[27] = data[33] = data[39] = data[45] = data[51] = data[57] = data[63] = data[69] = data[75] = data[81] = data[87] = data[93] = data[99] = secrets.MAC[3]
data[10] = data[16] = data[22] = data[28] = data[34] = data[40] = data[46] = data[52] = data[58] = data[64] = data[70] = data[76] = data[82] = data[88] = data[94] = data[100] = secrets.MAC[4]
data[11] = data[17] = data[23] = data[29] = data[35] = data[41] = data[47] = data[53] = data[59] = data[65] = data[71] = data[77] = data[83] = data[89] = data[95] = data[101] = secrets.MAC[5]

def wakePC():
    broadcast.sendto(data,sendhere)
    print('Magic Packet Sent')