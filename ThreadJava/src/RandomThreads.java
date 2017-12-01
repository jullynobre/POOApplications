import java.util.Random;

public class RandomThreads implements Runnable {
    private int quantity;

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public void run () {
        for (int i = 0; i < quantity; i++) {
            Random rnd = new Random();
            rnd.nextInt(3000);
        }
    }
}
