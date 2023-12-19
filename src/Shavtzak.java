import javax.swing.text.Position;
import java.util.ArrayList;
import java.util.Collections;

public class Shavtzak {

    private ArrayList<Guard> guards;
    private ArrayList<GuardPosition> positions;
    private ArrayList<ArrayList<Guard>> table;

    private int hour;
    private int minutes;

    private int timeToGuard;

    public Shavtzak (){
        guards = new ArrayList<>();
        positions = new ArrayList<>();
        table = new ArrayList<>();
    }

    public Shavtzak (int hour, int minutes, int timeToGuard){
        guards = new ArrayList<>();
        positions = new ArrayList<>();
        table = new ArrayList<>();
        this.hour =hour;
        this.minutes = minutes;
        this.timeToGuard = timeToGuard;
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
        table.add(new ArrayList<>());
    }

    public void randomOrder(ArrayList list){
        Collections.shuffle(list);
    }

    private ArrayList<String> createGuardHours(int hour, int minute, int minutesToGuard) {
        ArrayList<String> guardHours = new ArrayList<>();
        int count24 = 0;
        while (count24 < 24) {
            guardHours.add(String.format("%02d:%02d", hour, minute));

            for (int i = minutesToGuard; i > 0; i--) {
                minute++;
                if (minute == 60) {
                    minute = 0;
                    hour++;
                    count24++;
                    if (hour == 24)
                        hour = 0;

                }
            }
        }
        return guardHours;
    }

    public void guardList(){
        ArrayList<String> guardHours = createGuardHours(hour,minutes,timeToGuard);

        int indexGuard=0;
        for(int i=0;i<guardHours.size();i++){
            for(int j=0;j<positions.size();j++) {
                table.get(j).add(guards.get(indexGuard));
                indexGuard++;
                if (indexGuard == guards.size()) indexGuard = 0;
            }

        }
        for(int i=0;i < positions.size();i++){
            System.out.println(positions.get(i).getName());
            for(int j=0;j < table.get(i).size(); j++){
                System.out.print(guardHours.get(j)+" : ");
                System.out.println(table.get(i).get(j).getName());
            }
            System.out.println("----------");
        }
    }

}