public class GuardPosition {

    private String name;
    private int numOfGuards;

    public GuardPosition(String name, int numOfGuards){
        this.name = name;
        this.numOfGuards = numOfGuards;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getNumOfGuards() {
        return numOfGuards;
    }

    public void setNumOfGuards(int numOfGuards) {
        this.numOfGuards = numOfGuards;
    }
}


