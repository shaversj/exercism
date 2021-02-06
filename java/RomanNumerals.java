import java.util.Arrays;
import java.util.List;

class RomanNumeral {

    final List<Integer> baseValues = Arrays.asList(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1);
    final List<String> romanSymbols = Arrays.asList("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I");
    Integer number = 0;

    RomanNumeral (Integer number){
        this.number = number;
    }

    public String getRomanNumeral(){
        StringBuilder result = new StringBuilder();

        for(int index = 0; index < baseValues.size(); index++){
            Integer baseValue = baseValues.get(index);
            String symbol = romanSymbols.get(index);

            if(number >= baseValue){
                int quotient = number / baseValue;
                int remainder = number % baseValue;

                result.append(symbol.repeat(quotient));
                this.number = remainder;
            }
        }
        return result.toString();
    }
}