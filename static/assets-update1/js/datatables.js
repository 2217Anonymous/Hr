$(function(e) {
	
	//______Basic Data Table
	$('#basic-datatable').DataTable({
		language: {
			searchPlaceholder: 'Search...',
			sSearch: '',
		},
		lengthMenu: [
			[3, 25, 50, -1],
			[3, 25, 50, 'All'],
		],

	});	

	$('#department-datatable').DataTable({
		language: {
			searchPlaceholder: 'Search...',
			sSearch: '',
		},
		lengthMenu: [
			[3],
			[3],
		],
	});	


	$('#designation-datatable').DataTable({
		language: {
			searchPlaceholder: 'Search...',
			sSearch: '',
		},
		lengthMenu: [
			[6],
			[6],
		],
	});	

	//______Basic Data Table
	$('.responsive-datatable').DataTable({
		responsive: true,
		language: {
			searchPlaceholder: 'Search...',
			sSearch: '',
		}
	});

	//______Basic Data Table
	$('.manual-datatable').DataTable({
		responsive: true,
		language: {
			searchPlaceholder: 'Search...',
			sSearch: '',
		},
		lengthMenu: [
			[5],
			[5],
		],
	});

	//______File-Export Data Table
	var table = $('#file-datatable').DataTable({
		buttons: [ 'copy', 'excel', 'pdf', 'colvis' ],
		responsive: true,
		language: {
			searchPlaceholder: 'Search...',
			sSearch: '',
		}
	});
	table.buttons().container()
	.appendTo( '#file-datatable_wrapper .col-md-6:eq(0)' );	

	//______Delete Data Table
	var table = $('#delete-datatable').DataTable({
		language: {
			searchPlaceholder: 'Search...',
			sSearch: '',
		}
	}); 
    $('#delete-datatable tbody').on( 'click', 'tr', function () {
        if ( $(this).hasClass('selected') ) {
            $(this).removeClass('selected');
        }
        else {
            table.$('tr.selected').removeClass('selected');
            $(this).addClass('selected');
        }
    } );
    $('#button').click( function () {
        table.row('.selected').remove().draw( false );
    } );

	//______Details display datatable
	$('.details-datatable').DataTable( {
		responsive: true,
		language: {
			searchPlaceholder: 'Search...',
			sSearch: '',
		},
		responsive: {
			details: {
				display: $.fn.dataTable.Responsive.display.modal( {
					header: function ( row ) {
						var data = row.data();
						return 'Details for '+data[0]+' '+data[1];
					}
				} ),
				renderer: $.fn.dataTable.Responsive.renderer.tableAll( {
					tableClass: 'table border mb-0'
				} )
			}
		}
	} );

	//______Select2 
	$('.select2').select2({
		minimumResultsForSearch: Infinity
	});

});