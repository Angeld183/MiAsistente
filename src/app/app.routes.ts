import { Routes } from '@angular/router';
import { UploadComponent } from './components/upload/upload';

export const routes: Routes = [
  { path: '', component: UploadComponent },   // ruta raíz
  { path: 'upload', component: UploadComponent } // ruta explícita /upload
];