import java.awt.image.AreaAveragingScaleFilter;
import java.util.ArrayList;

public class GuardPosition {

    private String name;
    private int numOfGuards;
    private int timeToGuard;
    private int stopper;
    private ArrayList<String> guardList;

    public GuardPosition(String name, int numOfGuards,int timeToGuard){
        this.name = name;
        this.numOfGuards = numOfGuards;
        this.timeToGuard = timeToGuard;
        this.stopper = timeToGuard;
        this.guardList = new ArrayList<>();
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

    public void pass5Minutes(){
        stopper -= 5;
        if(stopper == 0) stopper =timeToGuard;
    }

    public ArrayList<String> getGuardList() {
        return guardList;
    }

    public void setGuardList(ArrayList<String> guardList) {
        this.guardList = guardList;
    }

    public boolean setGuards(){
        return stopper == timeToGuard;
    }

}


