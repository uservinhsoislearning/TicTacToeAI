import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Popup extends Frame{
      private TextField tfInput;
      private TextField tfOutput;
      public Popup(){
            setLayout(new GridLayout(2,2));
            add(new Label("Enter something:"));

            tfInput = new TextField(10);
            add(tfInput);
            tfInput.addActionListener(new TFInputListener());

            tfOutput = new TextField(10);
            tfOutput.setEditable(false);
            add(tfOutput);

            setTitle("I love your mom");
            setSize(350, 120);
            setVisible(true);
      }

      private class TFInputListener implements ActionListener {
            @Override
            public void actionPerfromed(ActionEvent event){
                  String inp = tfInput.getText();
                  tfInput.setText(inp);
                  tfOutput.setText(inp);
            }
      }
}
