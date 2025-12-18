import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { UploadComponent } from './components/upload/upload';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrls: ['./app.css']   // ✅ plural
})
export class App {
  protected readonly title = 'frontend-web';
}