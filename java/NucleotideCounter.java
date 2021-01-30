import java.util.Map;

public class NucleotideCounter {

    Map<Character, Integer> nucleotideMap = new java.util.HashMap<>(Map.of('A', 0, 'C', 0, 'G', 0, 'T', 0));
    String nucleotides = "";

    NucleotideCounter (String nucleotides) {

        if(nucleotides.length() != 0) {
            for (char letter : nucleotides.toCharArray()) {
                if (!nucleotideMap.containsKey(letter)){
                    throw new IllegalArgumentException();
                }
            }
        }
        this.nucleotides = nucleotides;
    }

    public Map<Character, Integer> nucleotideCounts () {
        for(char letter: nucleotides.toCharArray()){
            nucleotideMap.put(letter, nucleotideMap.get(letter) + 1);
        }
        return nucleotideMap;
    }

}