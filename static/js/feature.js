  $(document).ready(function() {

    $("#dt").datepicker({ 
      autoclose: true, 
      todayHighlight: true,
      dateFormat: 'yy-mm-dd'
    });
  } );
  $.ajax({
    url: "api/new_request/",
    type: 'GET',
        dataType: 'json', // added data type
        success: function(res) {
          console.log(res);
          for(i=0;i<res.length;i++)
          {
            thead  = `<tr>
            <td>`+res[i].client_id.name+`</td>
            <td>`+res[i].pro_area_id.product_name+`</td>
            <td>`+res[i].req_title+`</td>
            <td>`+res[i].req_description+`</td>
            <td>`+res[i].target_date+`</td>
            <td>`+res[i].req_priority+`</td>
            <td>`+res[i].status+`</td>
            </tr>
            `;  
            document.getElementById("table").innerHTML +=thead;
          }
          $('#request_list').DataTable();
        }
      });

  $.ajax({
    url: "api/client_list/",
    type: 'GET',
        dataType: 'json', // added data type
        success: function(res) {
          console.log(res);
          for(i=0;i<res.length;i++)
          {
            x = '<option value='+res[i].id+'>'+res[i].name+'</option>';
            document.getElementById("selectclient").innerHTML +=x;
            
          }
        }
      });

  $.ajax({
    url: "api/product_list/",
    type: 'GET',
        dataType: 'json', // added data type
        success: function(res) {
          console.log(res);
          for(i=0;i<res.length;i++)
          {
            y = '<option value='+res[i].id+'>'+res[i].product_name+'</option>';
            document.getElementById("selectproduct").innerHTML +=y;
            
          }
        }
      });

  function submit() {
    title = document.getElementById("title").value;
    desc = document.getElementById("desc").value;
    priority = document.getElementById("priority").value;
    date = document.getElementById("dt").value;
    client_id = document.getElementById("selectclient").value;
    pro_id = document.getElementById("selectproduct").value;
    data = 
    {
      "title": title,
      "description": desc,
      "c_id": client_id,
      "p_id": pro_id,
      "t_date": "2018-02-25",
      "req_priority": priority
    }
    $.ajax({
      url: "api/new_request/",
      type: 'POST',
        contentType: "application/json", // added data type
        dataType: 'json',
        data:JSON.stringify(data),
        success: function(res) {
          console.log(res);
          location.reload();
        },
        error: function(res) {
          console.log(res);
          location.reload();
        }
      });


  }
