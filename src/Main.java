public class Main {

    public static void main(String[] args) {
        Shavtzak s1 = new Shavtzak(14,0,60);
        Guard kfir = new Guard("Kfir");
        Guard roei = new Guard("Roei");
        Guard yona = new Guard("Yona");
        Guard maayan = new Guard("Maayan");
        Guard doek = new Guard("Doek");
        Guard moti = new Guard("Moti");
        Guard carmi = new Guard("Carmi");

        s1.addGuard(kfir);
        s1.addGuard(roei);
        s1.addGuard(yona);
        s1.addGuard(maayan);
        s1.addGuard(doek);
        s1.addGuard(moti);
        s1.addGuard(carmi);

        GuardPosition gp1  =new GuardPosition("Gate",1);
        GuardPosition gp2  =new GuardPosition("Patrol",1);

        s1.addPosition(gp1);
        s1.addPosition(gp2);

        s1.guardList();


    }
}
