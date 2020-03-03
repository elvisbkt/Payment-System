import { Component, OnInit } from '@angular/core';
declare var jQuery: any;

@Component({
  selector: 'app-payment-page',
  templateUrl: './payment-page.component.html',
  styleUrls: ['./payment-page.component.css']
})
export class PaymentPageComponent implements OnInit {

  constructor() { }

  ngOnInit() {
    (($) => {
      $('#sortable').change(() => {
        $('#table').bootstrapTable('refreshOptions', {
          sortable: $('#sortable').prop('checked')
        });
      });
    })(jQuery);
  }

}
