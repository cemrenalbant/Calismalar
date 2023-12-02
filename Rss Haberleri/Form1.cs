using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml;

namespace Rss_Haberleri
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            XmlTextReader xmloku = new XmlTextReader("https://www.milliyet.com.tr/rss/rssnew/dunyarss.xml");
            string selectedTitle = listBox1.SelectedItem.ToString();
            richTextBox1.Clear(); // Önceki içeriği temizle
                while (xmloku.Read())
                {
                    if (xmloku.NodeType == XmlNodeType.Element && xmloku.Name == "item")
                    {
                        string title = null;
                        string description = null;

                        while (xmloku.Read())
                        {
                            if (xmloku.NodeType == XmlNodeType.Element)
                            {
                                if (xmloku.Name == "title")
                                {
                                    title = xmloku.ReadString();
                                }
                                else if (xmloku.Name == "description" || xmloku.Name == "content")
                                {
                                    description = xmloku.ReadString();
                                }
                            }
                            else if (xmloku.NodeType == XmlNodeType.EndElement && xmloku.Name == "item")
                            {
                                if (title == selectedTitle)
                                {
                                    richTextBox1.Text = description;
                                }
                                break;
                            }
                        }
                    }
                }
            }

        private void button1_Click_1(object sender, EventArgs e)
        {

            XmlTextReader xmloku = new XmlTextReader("https://www.milliyet.com.tr/rss/rssnew/dunyarss.xml");
            {
                while (xmloku.Read())
                {
                    if (xmloku.Name == "title")
                    {
                        listBox1.Items.Add(xmloku.ReadString());
                    }
                }
            }
        }
    }
    }

