namespace WindowsFormsApp1
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.Gallery = new System.Windows.Forms.PictureBox();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.SelectPictureBtn = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.Gallery)).BeginInit();
            this.SuspendLayout();
            // 
            // Gallery
            // 
            this.Gallery.Location = new System.Drawing.Point(336, 12);
            this.Gallery.Name = "Gallery";
            this.Gallery.Size = new System.Drawing.Size(526, 475);
            this.Gallery.TabIndex = 0;
            this.Gallery.TabStop = false;
            this.Gallery.Click += new System.EventHandler(this.pictureBox1_Click);
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.FileName = "openFileDialog1";
            // 
            // SelectPictureBtn
            // 
            this.SelectPictureBtn.Location = new System.Drawing.Point(12, 138);
            this.SelectPictureBtn.Name = "SelectPictureBtn";
            this.SelectPictureBtn.Size = new System.Drawing.Size(113, 23);
            this.SelectPictureBtn.TabIndex = 1;
            this.SelectPictureBtn.Text = "Select Image";
            this.SelectPictureBtn.UseVisualStyleBackColor = true;
            this.SelectPictureBtn.Click += new System.EventHandler(this.SelectPictureBtn_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(874, 499);
            this.Controls.Add(this.SelectPictureBtn);
            this.Controls.Add(this.Gallery);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.Gallery)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox Gallery;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.Button SelectPictureBtn;
    }
}

