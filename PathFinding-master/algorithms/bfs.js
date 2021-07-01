
function node1(i,j){
    this.r=i;
    this.c=j;
    this.path = [];
}

// BFS
const bfs=async(isObstacle,start_i,start_j,end_i,end_j) =>{ 
    var rows=isObstacle.length;
    var cols=isObstacle[0].length;

    let nodes = new Array(rows);
    let visited = new Array(rows);
    for (let i = 0; i < rows; i++) {
        nodes[i] = new Array(cols);
        visited[i]=new Array(cols);
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            nodes[i][j] = new node1(i, j);
            visited[i][j]=false;
        }
    }
   

    let q = [];
    q.push([start_i,start_j]);
    visited[start_i][start_j] = true;

    let directions = ['top', 'bottom', 'left', 'right'];
    let diagonalDirections=['right-lower','right-upper','left-lower','left-upper']

    let diagonal = $('#diagonal').is(':checked');
    if(diagonal){
        directions= diagonalDirections.concat(directions);
    }

    while (q.length > 0) {
        let currentLocation = q.shift();
        let m=currentLocation[0];
        let n=currentLocation[1];

        if(m!=start_i || n!=start_j){
            document.getElementById('' + m + ',' + n).style.backgroundColor = '#97cafe';
        }

        //Explore all neighbours
        for (let i = 0; i < directions.length; i++) {
            let nr = m;
            let nc = n;
            let direction = directions[i];

            if (direction == 'top') {
                nr -= 1;
            } else if (direction == 'bottom') {
                nr += 1;
            } else if (direction == 'left') {
                nc -= 1;
            } else if (direction == 'right') {
                nc += 1;
            }else if(direction == 'left-upper'){
                nr-=1;
                nc-=1;
            }else if(direction == 'left-lower'){
                nr+=1;
                nc-=1;
            }else if(direction == 'right-upper'){
                nr-=1;
                nc+=1;
            }else if(direction == 'right-lower'){
                nr+=1;
                nc+=1;
            }

            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || isObstacle[nr][nc] == 1 || visited[nr][nc] == true) {
                // Not a valid point
                continue;
            }

            nodes[nr][nc].path = [...nodes[m][n].path];
            nodes[nr][nc].path.push(direction);


            if (nr == end_i && nc == end_j) {
                freezeClic=false;
                return nodes[nr][nc].path;
            }
            else {
                q.push([nr,nc]);
                document.getElementById('' + nr + ',' + nc).style.backgroundColor = '#cafafe';
                visited[nr][nc] = true;
            }

            await waitForSeconds(0.02);
        }

    }
    // empty path
    freezeClic=false;
    return [];

}


