/*
 * Created by SharpDevelop.
 * User: SCADA01
 * Date: 10/29/2019
 * Time: 2:48 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.IO; 
using System.Diagnostics;

using System.Drawing;
using System.Windows.Forms;

namespace bcl2
{
	/// <summary>
	/// Description of parameter.
	/// </summary>
	public partial class parameter : Form
	{
		public parameter()
		{
			//
			// The InitializeComponent() call is required for Windows Forms designer support.
			//
			InitializeComponent();
			
			//
			// TODO: Add constructor code after the InitializeComponent() call.
			//
		}
		void ParameterLoad(object sender, EventArgs e)
		{
			// full path of python interpreter  
			string python = @"C:\Python27\pythonw.exe";  
			              
			// python app to call  
			string myPythonApp = "C:\\Python27\\python-ku\\parameter.py";   
						
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
		}
	}
}
