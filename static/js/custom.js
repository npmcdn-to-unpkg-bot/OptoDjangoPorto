var map;

function initMap() {
    // Create an array of styles.
    var myLatLng = new google.maps.LatLng(46.523445, 6.899624);
    var styles = [
        {
            stylers: [
                { hue: "#00c0b5" },
                { saturation: -20 }
            ]
        },
        {
            featureType: "road",
            elementType: "geometry",
            stylers: [
                { lightness: 100 },
                { visibility: "simplified" }
            ]
        },
        {
            featureType: "road",
            elementType: "labels",
            stylers: [
                { visibility: "off" }
            ]
        }
    ];



    // Create a new StyledMapType object, passing it the array of styles,
    // as well as the name to be displayed on the map type control.
    var styledMap = new google.maps.StyledMapType(styles,{name: "Styled Map"});

    // Create a map object, and include the MapTypeId to add
    // to the map type control.
    var mapOptions = {
        zoom: 11,
        center: new google.maps.LatLng(46.523445, 6.899624),
        mapTypeControlOptions: {
            mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']
        }
    };
    var map = new google.maps.Map(document.getElementById('map'),
        mapOptions);

    //Associate the styled map with the MapTypeId and set it to display.
    map.mapTypes.set('map_style', styledMap);
    map.setMapTypeId('map_style');

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        icon: {
                path: google.maps.SymbolPath.BACKWARD_CLOSED_ARROW,
                scale: 4,
                strokeColor:'#00c0b5'
        },
        title: 'Opto Logic Technology S.A.'
    });

    var contentString =
    '<div id="content" class="panel" style="">'+
        '<a id="firstHeading" class="firstHeading"><img src="{% static '/media/img/logo_opto_250x51.png' %}"></a>'+
        '<div id="bodyContent">'+
            '<address class="" >'+
                '<br>'+
                '<div class="row">'+
                    '<div class="col-md-2">'+
                        'Route de Vevey 105<br>'+
                        '1618 Chatel-St-Denis<br>'+
                        'Switzerland<br>'+
                    '</div>'+
                    '<div class=uk-width-1-2>'+
                        '<a href="tel:+41219482080"><i class="fa fa-phone"></i>  +41 21 948 20 80</a>  <br>'+
                        '<a href="tel:+41219482088"><i class="fa fa-fax"></i> +41 21 948 20 88</a> <br><br>'+
                    '</div>'+
                '</div>'+
            '</address>'+
        '</div>'+
    '</div>';

    var infowindow = new google.maps.InfoWindow({
        content: contentString
    });

    marker.addListener('click', function() {
        infowindow.open(map, marker)
    });
    infowindow.open(map,marker);
    }
    google.setOnloadCallback(initMap);