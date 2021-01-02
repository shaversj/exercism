import java.math.BigInteger;

class Grains {

    BigInteger computeNumberOfGrainsOnSquare(final int square) {
        BigInteger numOfGrains = new BigInteger("2");

        if(square < 1 | square > 64){
            throw new IllegalArgumentException("square must be between 1 and 64");
        }

        if (square == 1 | square == 2){
            return BigInteger.valueOf(square);
        }

        for(int i = 2; i < square; i++){
            numOfGrains = numOfGrains.multiply(BigInteger.valueOf(2));
        }

        return numOfGrains;
    }

    BigInteger computeTotalNumberOfGrainsOnBoard() {
        BigInteger numOfGrains = new BigInteger("2");

        for(int i = 2; i < 65; i++){
            numOfGrains = numOfGrains.multiply(BigInteger.valueOf(2));

        }

        return numOfGrains.subtract(BigInteger.valueOf(1));
    }

}
