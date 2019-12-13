/*
 * Created by SharpDevelop.
 * User: SCADA01
 * Date: 1/17/2019
 * Time: 11:49 AM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.IO; 
using System.Diagnostics;

using System.Drawing;
using System.Windows.Forms;
using Sharp7Library;

namespace bcl2
{
	/// <summary>
	/// Description of MainForm.
	/// </summary>
	public partial class MainForm : Form
	{
		S7Client client;
//		Boolean warning_sound;
		
		public MainForm()
		{
			//
			// The InitializeComponent() call is required for Windows Forms designer support.
			//
			InitializeComponent();
			
			//
			// TODO: Add constructor code after the InitializeComponent() call.
			//
		}
		
		public static DialogResult InputBox(string title, string promptText, ref string value)
		{
		  Form form = new Form();
		  Label label = new Label();
		  TextBox textBox = new TextBox();
		  Button buttonOk = new Button();
		  Button buttonCancel = new Button();
		
		  form.Text = title;
		  label.Text = promptText;
		  textBox.Text = value;
		
		  buttonOk.Text = "OK";
		  buttonCancel.Text = "Cancel";
		  buttonOk.DialogResult = DialogResult.OK;
		  buttonCancel.DialogResult = DialogResult.Cancel;
		
		  label.SetBounds(9, 20, 372, 13);
		  textBox.SetBounds(12, 36, 372, 20);
		  buttonOk.SetBounds(228, 72, 75, 23);
		  buttonCancel.SetBounds(309, 72, 75, 23);
		
		  label.AutoSize = true;
		  textBox.Anchor = textBox.Anchor | AnchorStyles.Right;
		  buttonOk.Anchor = AnchorStyles.Bottom | AnchorStyles.Right;
		  buttonCancel.Anchor = AnchorStyles.Bottom | AnchorStyles.Right;
		
		  form.ClientSize = new Size(396, 107);
		  form.Controls.AddRange(new Control[] { label, textBox, buttonOk, buttonCancel });
		  form.ClientSize = new Size(Math.Max(300, label.Right + 10), form.ClientSize.Height);
		  form.FormBorderStyle = FormBorderStyle.FixedDialog;
		  form.StartPosition = FormStartPosition.CenterScreen;
		  form.MinimizeBox = false;
		  form.MaximizeBox = false;
		  form.AcceptButton = buttonOk;
		  form.CancelButton = buttonCancel;
		
		  DialogResult dialogResult = form.ShowDialog();
		  value = textBox.Text;
		  return dialogResult;
		}
		
		void MainFormLoad(object sender, EventArgs e)
		{
			// Create and connect the client
			client = new S7Client();
			int result = client.ConnectTo("192.168.0.180", 0, 1);
			Console.WriteLine("Connecting to 192.168.0.180");
			if(result == 0)
			{
//			    MessageBox.Show("Connected to 192.168.0.180");
//			    Console.WriteLine("Connected to 192.168.0.180");
			}
			else
			{
//			    Console.WriteLine(client.ErrorText(result));
//			    MessageBox.Show(client.ErrorText(result));
			}
			 
			// Disconnect the client
//			client.Disconnect();
			timer1.Enabled = true;
		}
		
		void Timer1Tick(object sender, EventArgs e)
		{
			try {
				exec_python();
			} catch (Exception ex) {
//				MessageBox.Show(ex.ToString());
//				throw;
			}
//			Thread t1 = new Thread(new ThreadStart(exec_python));
			// start newly created thread
//			t1.Start();
			cek();
			hitung_total_rate();
			hitung_total_flow();
		}
		
		void execute_python(int no)
		{
			// full path of python interpreter  
			string python = @"C:\Python27\pythonw.exe";  
			              
			// python app to call  
			string myPythonApp = "C:\\Python27\\python-ku\\c_interface.py";  
			  
			// dummy parameters to send Python script  
			int x = no;  

			
			// Create new process start info 
			ProcessStartInfo myProcessStartInfo = new ProcessStartInfo(python); 
			 
			// make sure we can read the output from stdout 
			myProcessStartInfo.UseShellExecute = false; 
			myProcessStartInfo.RedirectStandardOutput = true; 
			// start python app with 3 arguments  
			// 1st argument is pointer to itself, 2nd and 3rd are actual arguments we want to send 
			myProcessStartInfo.Arguments = myPythonApp + " " + x ;
			
			Process myProcess = new Process(); 
			// assign start information to the process 
			myProcess.StartInfo = myProcessStartInfo; 
			 
			// start process 
			myProcess.Start();
			
			// Read the standard output of the app we called.  
			StreamReader myStreamReader = myProcess.StandardOutput; 
			string myString = myStreamReader.ReadLine(); 
			             
			// wait exit signal from the app we called 
			myProcess.WaitForExit(); 
			 
			// close the process 
			myProcess.Close();
			Console.WriteLine("Value received from script: " + myString);
			string[] datas = myString.Split(' ');
			
			if(no==1){
				weight1.Text = datas[0];
				ratio1.Text = datas[1];
				sf1.Text = datas[2];
				af1.Text = datas[3];
				bs1.Text = datas[4];
				f1.Text = datas[5];
				
			}else if(no==2){
				weight2.Text = datas[0];
				ratio2.Text = datas[1];
				sf2.Text = datas[2];
				af2.Text = datas[3];
				bs2.Text = datas[4];
				f2.Text = datas[5];
				
			}else if(no==3){
				weight3.Text = datas[0];
				ratio3.Text = datas[1];
				sf3.Text = datas[2];
				af3.Text = datas[3];
				bs3.Text = datas[4];
				f3.Text = datas[5];
				
			}else if(no==4){
				weight4.Text = datas[0];
				ratio4.Text = datas[1];
				sf4.Text = datas[2];
				af4.Text = datas[3];
				bs4.Text = datas[4];
				f4.Text = datas[5];
				
			}else if(no==5){
				weight5.Text = datas[0];
				ratio5.Text = datas[1];
				sf5.Text = datas[2];
				af5.Text = datas[3];
				bs5.Text = datas[4];
				f5.Text = datas[5];
			}else if(no==6){
				weight6.Text = datas[0];
				ratio6.Text = datas[1];
				sf6.Text = datas[2];
				af6.Text = datas[3];
				bs6.Text = datas[4];
				f6.Text = datas[5];
			}else if(no==7){
				weight7.Text = datas[0];
				ratio7.Text = datas[1];
				sf7.Text = datas[2];
				af7.Text = datas[3];
				bs7.Text = datas[4];
				f7.Text = datas[5];				
			}
		}

		void exec_python()
		{
			// full path of python interpreter  
			string python = @"C:\Python27\pythonw.exe";  
			              
			// python app to call  
			string myPythonApp = "C:\\Python27\\python-ku\\coba.py";   
						
			// Create new process start info 
			ProcessStartInfo myProcessStartInfo = new ProcessStartInfo(python); 
			 
			// make sure we can read the output from stdout 
			myProcessStartInfo.UseShellExecute = false; 
			myProcessStartInfo.RedirectStandardOutput = true; 
			// start python app with 3 arguments  
			// 1st argument is pointer to itself, 2nd and 3rd are actual arguments we want to send 
			myProcessStartInfo.Arguments = myPythonApp;
			
			Process myProcess = new Process(); 
			// assign start information to the process 
			myProcess.StartInfo = myProcessStartInfo; 
			 
			// start process 
			myProcess.Start();
			
			// Read the standard output of the app we called.  
			StreamReader myStreamReader = myProcess.StandardOutput; 
			string myString = myStreamReader.ReadLine(); 
			             
			// wait exit signal from the app we called 
			myProcess.WaitForExit(); 
			 
			// close the process 
			myProcess.Close();
			Console.WriteLine("Value received from script: " + myString);
			
			string[] datas = myString.Split(':');
			string[] data1 = datas[0].Trim(' ').Split(' ');
			string[] data2 = datas[1].Trim(' ').Split(' ');
			string[] data3 = datas[2].Trim(' ').Split(' ');
			string[] data4 = datas[3].Trim(' ').Split(' ');
			string[] data5 = datas[4].Trim(' ').Split(' ');
			string[] data6 = datas[5].Trim(' ').Split(' ');
			string[] data7 = datas[6].Trim(' ').Split(' ');
			string[] parameter = datas[7].Trim(' ').Split(' ');
			
			weight1.Text = data1[0];
			ratio1.Text = data1[1];
			sf1.Text = data1[2];
			af1.Text = data1[3];
			bs1.Text = data1[4];
			f1.Text = data1[5];
			
			weight2.Text = data2[0];
			ratio2.Text = data2[1];
			sf2.Text = data2[2];
			af2.Text = data2[3];
			bs2.Text = data2[4];
			f2.Text = data2[5];
			
			weight3.Text = data3[0];
			ratio3.Text = data3[1];
			sf3.Text = data3[2];
			af3.Text = data3[3];
			bs3.Text = data3[4];
			f3.Text = data3[5];
			
			weight4.Text = data4[0];
			ratio4.Text = data4[1];
			sf4.Text = data4[2];
			af4.Text = data4[3];
			bs4.Text = data4[4];
			f4.Text = data4[5];
			
			weight5.Text = data5[0];
			ratio5.Text = data5[1];
			sf5.Text = data5[2];
			af5.Text = data5[3];
			bs5.Text = data5[4];
			f5.Text = data5[5];
			
			weight6.Text = data6[0];
			ratio6.Text = data6[1];
			sf6.Text = data6[2];
			af6.Text = data6[3];
			bs6.Text = data6[4];
			f6.Text = data6[5];
			
			weight7.Text = data7[0];
			ratio7.Text = data7[1];
			sf7.Text = data7[2];
			af7.Text = data7[3];
			bs7.Text = data7[4];
			f7.Text = data7[5];	

			shift_capacity.Text = parameter[0];
			//actual_flow.Text = parameter[1];
	            
		}
		
		void cek(){
			double c1 = Convert.ToDouble(af1.Text) / Convert.ToDouble(sf1.Text);
			double c2 = Convert.ToDouble(af2.Text) / Convert.ToDouble(sf2.Text);
			double c3 = Convert.ToDouble(af3.Text) / Convert.ToDouble(sf3.Text);
			double c4 = Convert.ToDouble(af4.Text) / Convert.ToDouble(sf4.Text);
			double c5 = Convert.ToDouble(af5.Text) / Convert.ToDouble(sf5.Text);
			double c6 = Convert.ToDouble(af6.Text) / Convert.ToDouble(sf6.Text);
			double c7 = Convert.ToDouble(af7.Text) / Convert.ToDouble(sf7.Text);
			int err = 0;
			if(c1>1.05 || c1<0.95) { groupBox1.BackColor = Color.Red; if(alarm1.Checked){ err++; }} else { groupBox1.BackColor = Color.Green;}
			if(c2>1.05 || c2<0.95) { groupBox2.BackColor = Color.Red; if(alarm2.Checked){ err++; }} else { groupBox2.BackColor = Color.Green;}
			if(c3>1.05 || c3<0.95) { groupBox3.BackColor = Color.Red; if(alarm3.Checked){ err++; }} else { groupBox3.BackColor = Color.Green;}
			if(c4>1.05 || c4<0.95) { groupBox4.BackColor = Color.Red; if(alarm4.Checked){ err++; }} else { groupBox4.BackColor = Color.Green;}
			if(c5>1.05 || c5<0.95) { groupBox5.BackColor = Color.Red; if(alarm5.Checked){ err++; }} else { groupBox5.BackColor = Color.Green;}
			if(c6>1.05 || c6<0.95) { groupBox6.BackColor = Color.Red; if(alarm6.Checked){ err++; }} else { groupBox6.BackColor = Color.Green;}
			if(c7>1.05 || c7<0.95) { groupBox7.BackColor = Color.Red; if(alarm7.Checked){ err++; }} else { groupBox7.BackColor = Color.Green;}
			
			if(err!=0){
				warning_sound();
			}
		}
		
		void hitung_total_rate(){
			double total = Convert.ToDouble(ratio1.Text) + Convert.ToDouble(ratio2.Text) + Convert.ToDouble(ratio3.Text) + Convert.ToDouble(ratio4.Text) + Convert.ToDouble(ratio5.Text) + Convert.ToDouble(ratio6.Text) + Convert.ToDouble(ratio7.Text);
			                                                                                                                                                                                
			total_ratio.Text = total.ToString();
		}
		
		void hitung_total_flow(){
			double total = Convert.ToDouble(af1.Text) + Convert.ToDouble(af2.Text) + Convert.ToDouble(af3.Text) + Convert.ToDouble(af4.Text) + Convert.ToDouble(af5.Text) + Convert.ToDouble(af6.Text) + Convert.ToDouble(af7.Text);
			total = ( total * 60 )/1000;
			actual_flow.Text = total.ToString("#.##");
		}
		
		
		void set(string command,string number,string value)
		{
			// full path of python interpreter  
			string python = @"C:\Python27\pythonw.exe";  
			              
			// python app to call  
			string myPythonApp = "C:\\Python27\\python-ku\\setter.py";   
						
			// Create new process start info 
			ProcessStartInfo myProcessStartInfo = new ProcessStartInfo(python); 
			 
			// make sure we can read the output from stdout 
			myProcessStartInfo.UseShellExecute = false; 
			myProcessStartInfo.RedirectStandardOutput = true; 
			// start python app with 3 arguments  
			// 1st argument is pointer to itself, 2nd and 3rd are actual arguments we want to send 
			myProcessStartInfo.Arguments = myPythonApp +" "+command+" "+number+" "+value;
			
			Process myProcess = new Process(); 
			// assign start information to the process 
			myProcess.StartInfo = myProcessStartInfo; 
			 
			// start process 
			myProcess.Start();
		
		}
		
		void Ratio1Click(object sender, EventArgs e)
		{
//			InputBox("masukkan nilai untuk rasio weigher 1","","");

			string value = "Ratio 1";
			if (InputBox("Ratio", "Input Ratio 1:", ref value) == DialogResult.OK)
			{
				MessageBox.Show(value);
//				set("ratio","1",value);
			}
		}		
		
		void Ratio2Click(object sender, EventArgs e)
		{
	
		}
		void Ratio3Click(object sender, EventArgs e)
		{
	
		}
		void Ratio4Click(object sender, EventArgs e)
		{
	
		}
		void Ratio5Click(object sender, EventArgs e)
		{
	
		}
		void Ratio6Click(object sender, EventArgs e)
		{
	
		}
		void Ratio7Click(object sender, EventArgs e)
		{
	
		}
		void Shift_capacityTextChanged(object sender, EventArgs e)
		{
	
		}
		void Button1Click(object sender, EventArgs e)
		{
//			this.Hide();
			parameter par = new parameter();
			par.Show();		
		}
		
		void warning_sound(){
			System.Media.SoundPlayer player = new System.Media.SoundPlayer(@"C:\\Python27\\python-ku\\sound.wav");
			player.Play();	
		}
		void GroupBox1Enter(object sender, EventArgs e)
		{
	
		}


	}
}
