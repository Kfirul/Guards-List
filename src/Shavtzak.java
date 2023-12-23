import javax.swing.text.Position;
import java.util.ArrayList;
import java.util.Collections;

public class Shavtzak {

    private ArrayList<Guard> guards;
    private ArrayList<GuardPosition> positions;

    private ArrayList<String> time =new ArrayList<>();

    private int hour;
    private int minutes;


    public Shavtzak (){
        guards = new ArrayList<>();
        positions = new ArrayList<>();
        createClock(0,0);
    }

    public Shavtzak (int hour, int minutes){
        guards = new ArrayList<>();
        positions = new ArrayList<>();
        this.hour =hour;
        this.minutes = minutes;
        createClock(hour,minutes);
    }

    public ArrayList<Guard> getGuards() {
        return guards;
    }

    public void setGuards(ArrayList<Guard> guards) {
        this.guards = guards;
    }

    public ArrayList<GuardPosition> getPositions() {
        return positions;
    }

    public void setPositions(ArrayList<GuardPosition> positions) {
        this.positions = positions;
    }

    public void addGuard(Guard guard){
        guards.add(guard);
    }

    public void addPosition(GuardPosition position){
        positions.add(position);

    }

    public void randomOrder(ArrayList list){
        Collections.shuffle(list);
    }

    public void createGuardList(){

        int indexGuard=0;
        for(int i=0;i<time.size();i++){
            for(int j=0;j<positions.size();j++) {
                String guardsNames ="";

                if(positions.get(j).setGuards()) {
                    guardsNames += time.get(i)+ " : ";
                    for (int z = 0; z < positions.get(j).getNumOfGuards(); z++) {
                        guardsNames += guards.get(indexGuard).getName() + " ";
                        indexGuard++;
                        if (indexGuard == guards.size()) indexGuard = 0;
                    }
                    positions.get(j).getGuardList().add(guardsNames);
                }
                positions.get(j).pass5Minutes();

            }

        }

        }

        public void printList() {
            for (int i = 0; i < positions.size(); i++) {
                System.out.println(positions.get(i).getName());
                System.out.println(positions.get(i).getGuardList());

                }
                System.out.println("----------");
            }


    private void createClock(int hour,int minute){
        int count24 = 0;
        while (count24 < 24) {
            time.add(String.format("%02d:%02d", hour, minute));
            minute = minute +5;
            if (minute == 60) {
                minute = 0;
                hour++;
                count24++;
                if (hour == 24)
                    hour = 0;
            }
        }
    }

}