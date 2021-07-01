
// Instructions
function showInstructions() {
    alert("1) Use Box Click to specify the required points in the grid.\n2) Green point indicates the starting point.\n3) Red point indicates the end point.\n4) Choose an algorithm from the given options.\n5) Click on 'Find Path' to start the search.");
}

// Grid
var isObstacle = [];  // To keep track of obstacles's locations
var rows = 35;        // number of rows of grid
var cols = 35;        // number of columns of grid
var mxRows = 35;      // maximum number of rows of grid
var mxCols = 35;      // maximum number of cols of grid

if (screen.width < 650) {
    rows = 20;
    cols = 20;
    mxRows = 20;
    mxCols = 20;
    $("#numberOfRows").attr({
        "max": mxRows,
        "min": 1
    });
    $("#numberOfCols").attr({
        "max": mxCols,
        "min": 1
    });
    $('#numberOfRows').val(20);
    $('#numberOfCols').val(20);
}

var start_i;
var start_j;
var end_i;
var end_j;

var gridBoxes = "";   // Boxes inside the grid


createGrid();

// Create Grid 
function createGrid() {

    isObstacle.splice(0);

    start_i = 0;
    start_j = 0;
    end_i = rows - 1;
    end_j = cols - 1;


    for (let i = 0; i < rows; i++) {
        let row = [];
        for (let j = 0; j < cols; j++) {
            row.push(0);
        }

        isObstacle.push(row);
    }


    var i, j;
    for (i = 0; i < rows; i++) {
        let rowBoxes = "";

        for (j = 0; j < cols; j++) {
            rowBoxes += '<div class=\"box\" id=\"' + i + ',' + j + '\" onclick = \"boxClick(' + i + ',' + j + ')\" ></div>';
        }

        gridBoxes += '<div class="gridRow">' + rowBoxes + '</div>';
    }

    $('#grid').append(gridBoxes);


    document.getElementById('' + start_i + ',' + start_j).style.backgroundColor = '#14a76c';
    document.getElementById('' + end_i + ',' + end_j).style.backgroundColor = '#ff6525';

}

// Reset Grid
function changeGridSize() {

    rows = $('#numberOfRows').val();
    cols = $('#numberOfCols').val();

    if ((rows > mxRows) || (cols > mxCols)) {
        rows = mxRows;
        cols = mxCols;
        alert('Maximum allowed Grid Rows is: ' + mxRows + '\nMaximum allowed Grid Columns is: ' + mxCols);
        $('#numberOfRows').val(rows);
        $('#numberOfCols').val(cols);
    }

    gridBoxes = "";
    $('#grid').empty();
    $('#svgBox').empty();
    createGrid();
}

// Handling Box Click
function boxClick(i, j) {
    changeBoxColor(i, j);
    arrayManipulator(i, j);
}

function changeBoxColor(i, j) {
    var mouseTip = $('#mouseTip').val();

    switch (mouseTip) {
        case 'obstacle':
            if ((i != start_i || j != start_j) && (i != end_i || j != end_j) && isObstacle[i][j] == 0) {
                // if the box is not the source or destination point or not an obstacle then mark it as an obstacle
                document.getElementById('' + i + ',' + j).style.backgroundColor = '#746e6e';
            }
            else if (isObstacle[i][j] == 1) {
                // if the box is an obstacle  then remove the obstacle
                document.getElementById('' + i + ',' + j).style.backgroundColor = 'white';
            }
            break;
        case 'source':
            if ((i != end_i || j != end_j) && (i != start_i || j != start_j)) {
                // if the box is not the source or the destination , then change the source point
                document.getElementById('' + start_i + ',' + start_j).style.backgroundColor = 'white';
                document.getElementById('' + i + ',' + j).style.backgroundColor = '#14a76c';
            }
            break;
        case 'destination':
            if ((i != end_i || j != end_j) && (i != start_i || j != start_j)) {
                // if the box is not the source or the destination , then change the destination point
                document.getElementById('' + end_i + ',' + end_j).style.backgroundColor = 'white';
                document.getElementById('' + i + ',' + j).style.backgroundColor = '#ff6525';
            }
            break;
        default:

    }
}

function arrayManipulator(i, j) {
    var mouseTip = $('#mouseTip').val();

    switch (mouseTip) {
        case 'obstacle':
            if ((i != start_i || j != start_j) && (i != end_i || j != end_j) && isObstacle[i][j] == 0) {
                // if the box is not the source or destination point or not an obstacle then mark it as an obstacle
                isObstacle[i][j] = 1;
            }
            else if (isObstacle[i][j] == 1) {
                // if the box is an obstacle  then remove the obstacle
                isObstacle[i][j] = 0;
            }
            break;
        case 'source':
            if ((i != end_i || j != end_j) && (i != start_i || j != start_j)) {
                // if the box is not the source or the destination , then change the source point
                start_i = i;
                start_j = j;
                isObstacle[i][j] = 0;
            }
            break;
        case 'destination':
            if ((i != end_i || j != end_j) && (i != start_i || j != start_j)) {
                // if the box is not the source or the destination , then change the destination point
                end_i = i;
                end_j = j;
                isObstacle[i][j] = 0;
            }
            break;
        default:

    }
}



// Find the shortest Path
const waitForSeconds = (secs) => {
    return new Promise(resolve => {
        setTimeout(resolve, secs * 1000);
    })
}

// // To avoid multiple find paths
let freezeClic = false; // just modify that variable to disable all clics events

document.addEventListener("click", e => {
    if (freezeClic) {
        e.stopImmediatePropagation();
        e.preventDefault();
    }
}, true);



const findPath = async () => {
    removePreviousPath();

    let path = [];
    let promise;
    let algo = $('#algo').val();

    freezeClic = true;

    if (algo == 'bfs') {
        promise = bfs(isObstacle, start_i, start_j, end_i, end_j);
    }
    else if (algo == 'dijkstra') {
        promise = dijkstra(isObstacle, start_i, start_j, end_i, end_j);
    }
    else if (algo == 'astar') {
        // alert('Note that - Although being the best pathfinding algorithm around, A* Algorithm doesn’t produce the shortest path always, as it relies heavily on heuristics / approximations to calculate.');
        promise = astar(isObstacle, start_i, start_j, end_i, end_j);
    }


    promise.then(
        function (value) {
            path = value;
            if (path.length > 0) {
                changePathColour(path);
                drawPath(path);
            }
            else {
                alert('No path exists between starting and ending point. Please try for another arrangement!');
            }
        }
    );


}


function removePreviousPath() {
    $('#svgBox').empty();
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (isObstacle[i][j] == 1) {
                document.getElementById('' + i + ',' + j).style.backgroundColor = '#746e6e';
            }
            else if ((i == start_i) && (j == start_j)) {
                document.getElementById('' + i + ',' + j).style.backgroundColor = '#14a76c';
            }
            else if (i == end_i && j == end_j) {
                document.getElementById('' + i + ',' + j).style.backgroundColor = '#ff6525';
            }
            else {
                document.getElementById('' + i + ',' + j).style.backgroundColor = 'white';
            }
        }
    }
}

function changePathColour(path) {
    let i = start_i, j = start_j;
    for (let a = 0; a < path.length; a++) {
        if (path[a] == 'top') {
            i -= 1;
        } else if (path[a] == 'bottom') {
            i += 1;
        } else if (path[a] == 'left') {
            j -= 1;
        } else if (path[a] == 'right') {
            j += 1;
        } else if (path[a] == 'left-upper') {
            i -= 1;
            j -= 1;
        } else if (path[a] == 'left-lower') {
            i += 1;
            j -= 1;
        } else if (path[a] == 'right-upper') {
            i -= 1;
            j += 1;
        } else if (path[a] == 'right-lower') {
            i += 1;
            j += 1;
        }

        if ((i != start_i || j != start_j) && (i != end_i || j != end_j)) {
            document.getElementById('' + i + ',' + j).style.backgroundColor = '#ffe400';
        }
    }
}

function drawPath(path) {
    let boxWidth = $('.box').width();
    let boxHeight = $('.box').height();
    boxWidth += 2;
    boxHeight += 2;

    let point = [(start_i * boxHeight + boxHeight / 2), (start_j * boxWidth + boxWidth / 2)];

    let line = '<polyline points=\"' + point[1] + ',' + point[0] + ' ';
    for (let a = 0; a < path.length; a++) {
        if (path[a] == 'top') {
            // i -= 1;
            point[0] -= boxHeight;
        } else if (path[a] == 'bottom') {
            // i += 1;
            point[0] += boxHeight;
        } else if (path[a] == 'left') {
            // j -= 1;
            point[1] -= boxWidth;
        } else if (path[a] == 'right') {
            // j += 1;
            point[1] += boxWidth;
        } else if (path[a] == 'left-upper') {
            // i-=1;
            // j-=1;
            point[0] -= boxHeight;
            point[1] -= boxWidth;
        } else if (path[a] == 'left-lower') {
            // i+=1;
            // j-=1;
            point[0] += boxHeight;
            point[1] -= boxWidth;
        } else if (path[a] == 'right-upper') {
            // i-=1;
            // j+=1;
            point[0] -= boxHeight;
            point[1] += boxWidth;
        } else if (path[a] == 'right-lower') {
            // i+=1;
            // j+=1;
            point[0] += boxHeight;
            point[1] += boxWidth;
        }
        line += (point[1] + ',' + point[0] + ' ');

    }

    line += '\" style=\"fill:none; stroke:black; stroke-width:3\">'


    let svgPath = '<svg id=\"svgPath\">' + line + '</svg>';
    $('#svgBox').append(svgPath);

    // SVM Path grid
    let h = $('#grid').height();
    let w = $('#grid').width();

    $('#svgPath').attr('height', h);
    $('#svgPath').attr('width', w);
    let m = $("#grid").css("margin");
    $('#svgBox').css('margin', m);

}