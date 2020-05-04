import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.lang.*;
import java.util.*;
import java.io.*;
public class Test extends JFrame{
	public static void main(String args[]){
		new Test();
	}
	private Image img;
	private Image img2;
	GridBagConstraints gbc = new GridBagConstraints();
	private JButton btn1;
	private JButton btn2;
	public Test(){
		super("Welcome!");
		img = new ImageIcon("sample.jpg").getImage();
		JPanel container = new MyBackground();
		JLabel label = new JLabel();
		label.setIcon(new ImageIcon("exp.png"));
		gbc.gridx=0;
		gbc.gridy=0;
		gbc.gridwidth=4;
		gbc.fill = GridBagConstraints.HORIZONTAL;
		container.add(label,gbc);
		Font f = new Font("BaskervilleOldFace",Font.BOLD + Font.ITALIC,25);
		JLabel label2 = new JLabel();
		label2.setFont(f);
		label2.setForeground(Color.MAGENTA);
		label2.setBounds(80,20,250,80);
		label2.setText("- the handwritten calculator");
		gbc.gridx=3;
		gbc.gridy=3;
		container.add(label2,gbc);
		gbc.gridx=0;
		gbc.gridy=10;
		btn1 = new JButton("Child Mode");
		btn1.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent arg0){
				try{
					Process p =Runtime.getRuntime().exec("python child.py");
					p.waitFor();
				}catch(Exception e){System.out.println(e);}
			}
		});
		container.add(btn1,gbc);
		gbc.gridx=0;
		gbc.gridy=12;
		btn2=new JButton("Calculator Mode");
		btn2.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent arg0){
				try{
					Process p =Runtime.getRuntime().exec("python calc_mode.py");
					p.waitFor();
				}catch(Exception e){System.out.println(e);}
			}
		});
		container.add(btn2,gbc);
		add(container);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setSize(800,500);
		setVisible(true);
	}
	public class MyBackground extends JPanel{;
		public MyBackground(){
			setBackground(new Color(0,true));
			setLayout(new GridBagLayout());
		}
		public void paintComponent(Graphics g){
			g.drawImage(img,0,0,getWidth(),getHeight(),this);
			super.paintComponent(g);
		}
	}
}
		