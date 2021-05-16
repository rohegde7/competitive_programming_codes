class NumberOf1Bits {

    public static void main(String[] args) {
        
        numberOfSetBits(10);
    }

    public static int numberOfSetBits(long a) {

            // apply n&(n-1) till we eliminate all the least significant bit

            int numberOf1Bits = 0;

            while(a != 0) {
                
                numberOf1Bits++;

                a = a & (a-1);
            }

            System.out.println("Number of set bits: " + numberOf1Bits);

            return numberOf1Bits;
	}
}