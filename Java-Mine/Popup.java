import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Popup{
      private JFrame textFrame;
      public Popup(){
            textFrame = new JFrame("Minesweeper");
            textFrame.setSize(350,120);
            textFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            textFrame.setResizable(false);
            textFrame.setLocationRelativeTo(null);

            JPanel panel = new JPanel(new GridLayout(2,2));
            panel.add(new Label("Enter the size of your board"));
            panel.add(new JTextField());
            panel.add(new Label("Enter the number of bombs"));
            panel.add(new JTextField());

            // Adding the panel in the end after completed everything.
            textFrame.add(panel);
            textFrame.setVisible(true);
      }
}
