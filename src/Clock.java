import java.util.ArrayList;

    public class Clock {
        private int hour;
        private int minute;
        private int minutesToGuard;

        public Clock(int hour, int minute, int minutesToGuard) {
            this.hour = hour;
            this.minute = minute;
            this.minutesToGuard = minutesToGuard;
        }

        public ArrayList<String> createGuardHours() {
            ArrayList<String> guardHours = new ArrayList<>();
            int count24 = 0;
            while (count24 < 24) {
                guardHours.add(String.format("%02d:%02d", hour, minute));

                for (int i = minutesToGuard; i > 0; i--) {
                    minute++;
                    if (minute == 60) {
                        minute = 0;
                        hour++;
                        if (hour == 24) {
                            hour = 0;
                            count24++;
                        }
                    }
                }
            }
            return guardHours;
        }


    }



