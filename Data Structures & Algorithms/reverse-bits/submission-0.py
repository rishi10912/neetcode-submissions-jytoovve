class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:]
        #amke usre it is 32 bit by filling in zeroes
        bits=bits.zfill(32)
        bits=bits[::-1]
        return int(bits,2)

        