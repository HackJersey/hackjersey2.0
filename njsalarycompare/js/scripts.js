
  $(document).ready(function(){
      var geocoder = new google.maps.Geocoder();

      if(!navigator.geolocation){
        output.innerHTML = "<p>Geolocation is not supported in your browser!</p><br><br>";
        return;
      }

      function success(position) {
        var lat = position.coords.latitude || 40.00;
        var lng = position.coords.longitude || -74.65;

        var queryStr = "http://boundary.hackjersey.com/1.0/boundary/?contains=" + lat +"," + lng + "&sets=new-jersey-municipalities";

        var latlng = new google.maps.LatLng(lat, lng);

        var mapOptions = {
          center: latlng,
          scrollWheel: false,
          zoom: 10
        };
        
        var marker = new google.maps.Marker({
          position: latlng,
          url: '/',
          animation: google.maps.Animation.DROP
        });
        
        var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
        marker.setMap(map);


        $.ajax({
          type : "GET",
          url : queryStr,
          dataType : "jsonp",
          crossDomain : true,
          headers : {"Access-Control-Allow-Origin" : "*"}
        }).done(function(data, textStatus, jqXHR){
          //console.log(data.objects[0]);
          for(var prop in fipData){
            if(data.objects[0].metadata.KEY.indexOf(prop) > -1) {
             $("#locText").html("You are in " + data.objects[0].name + ". See how the median salary for " + fipData[prop].COUNTY + " residents compares to state, county and local public employees.");
             $("#over").html("$" + fipData[prop].OVERALL.toLocaleString());
             $("#state").html("$" + fipData[prop].STATEWIDE.toLocaleString());
             $("#fire").html("$" + fipData[prop].FIRE.toLocaleString());
             $("#police").html("$" + fipData[prop].POLICE.toLocaleString());             
             $("#public").html("$" + fipData[prop].PUBLIC_EMPLOYEES.toLocaleString());             
             $("#teach").html("$" + fipData[prop].TEACHERS.toLocaleString());             

             //console.log(fipData[prop]);
            }
          }
        });
      }

      function error(){
        //output.innerHTML = "Unable to retrieve your location";
      }
      
      navigator.geolocation.getCurrentPosition(success, error);

      $("#addressInput").on("keydown", function(e){
        if(e.keyCode == 13) {
          e.preventDefault();
          
          var address = $(this).val();

          geocoder.geocode( { 'address': address}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
              //console.log(results[0].geometry.location);
              var lat = results[0].geometry.location.k;
              var lng = results[0].geometry.location.D;

              var queryStr = "http://boundary.hackjersey.com/1.0/boundary/?contains=" + lat +"," + lng + "&sets=new-jersey-municipalities";

              var latlng = new google.maps.LatLng(lat, lng);

              var mapOptions = {
                center: latlng,
                scrollWheel: false,
                zoom: 10
              };
              
              var marker = new google.maps.Marker({
                position: latlng,
                url: '/',
                animation: google.maps.Animation.DROP
              });
              
              var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
              marker.setMap(map);

              $.ajax({
                type : "GET",
                url : queryStr,
                dataType : "jsonp",
                crossDomain : true,
                headers : {"Access-Control-Allow-Origin" : "*"}
              }).done(function(data, textStatus, jqXHR){
                //console.log(data);
                for(var prop in fipData){
                  if(data.objects[0].metadata.KEY.indexOf(prop) > -1) {
                    $("#locText").html("You are in " + data.objects[0].name + ". See how the median salary for " + fipData[prop].COUNTY + " residents compares to state, county and local public employees.");
                    $("#over").text("$" + fipData[prop].OVERALL.toLocaleString());
                    //console.log("$" + fipData[prop].OVERALL.toLocaleString());
                    $("#state").text("$" + fipData[prop].STATEWIDE.toLocaleString());
                    $("#fire").text("$" + fipData[prop].FIRE.toLocaleString());
                    $("#police").text("$" + fipData[prop].POLICE.toLocaleString());             
                    $("#public").text("$" + fipData[prop].PUBLIC_EMPLOYEES.toLocaleString());             
                    $("#teach").text("$" + fipData[prop].TEACHERS.toLocaleString());
                  }
                }
              });
            } else {
              alert("Geocode was not successful for the following reason: " + status);
            }
          });
        }
      });
    });
