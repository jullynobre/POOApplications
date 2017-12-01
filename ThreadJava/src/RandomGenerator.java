import java.util.Random;

public class RandomGenerator {
    public static void main(String[] args) {
        long start1Thread = System.currentTimeMillis(); random1Thread();
        long elapsed1Thread = System.currentTimeMillis() - start1Thread;
        long start3Thread = System.currentTimeMillis(); random3Thread();
        long elapsed3Thread = System.currentTimeMillis() - start3Thread;

        System.out.println("Time to run with 1 thread: " + elapsed1Thread);
        System.out.println("Time to run with 3 threads: " + elapsed3Thread);
    }
    public static void random3Thread(){
        RandomThreads rt1 = new RandomThreads();
        rt1.setQuantity(1000);
        Thread t1 = new Thread(rt1);
        t1.start();

        RandomThreads rt2 = new RandomThreads();
        rt2.setQuantity(1000);
        Thread t2 = new Thread(rt2);
        t2.start();

        RandomThreads rt3 = new RandomThreads();
        rt3.setQuantity(1000);
        Thread t3 = new Thread(rt3);
        t3.start();
    }
    public static void random1Thread(){
        for (int i = 0; i < 3000; i++){
            Random rnd = new Random();
            rnd.nextInt(3000);
        }
    }
}

