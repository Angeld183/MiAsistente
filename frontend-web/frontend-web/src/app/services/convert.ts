import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class ConvertService {
  private baseUrl = 'https://miasistente.onrender.com/docs';

  constructor(private http: HttpClient) {}

  pdfToDocx(file: File) {
    const form = new FormData();
    form.append('file', file);
    return this.http.post(`${this.baseUrl}/pdf-to-docx`, form, { responseType: 'blob' });
  }

  docxToPdf(file: File) {
    const form = new FormData();
    form.append('file', file);
    return this.http.post(`${this.baseUrl}/docx-to-pdf`, form, { responseType: 'blob' });
  }
}