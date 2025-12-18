import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ConvertService } from '../../services/convert';

@Component({
  selector: 'app-upload',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './upload.html',
  styleUrls: ['./upload.css']
})
export class UploadComponent {
  selectedFile: File | null = null;

  constructor(private convertService: ConvertService) {}

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  convertDocxToPdf() {
    if (this.selectedFile) {
      this.convertService.docxToPdf(this.selectedFile).subscribe(blob => {
        this.downloadFile(blob, 'converted.pdf');
      });
    }
  }

  convertPdfToDocx() {
    if (this.selectedFile) {
      this.convertService.pdfToDocx(this.selectedFile).subscribe(blob => {
        this.downloadFile(blob, 'converted.docx');
      });
    }
  }

  private downloadFile(blob: Blob, filename: string) {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    window.URL.revokeObjectURL(url);
  }
}