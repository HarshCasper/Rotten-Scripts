

const getRepoFromStarred = () => {

}

const getRepoViaMethod = (method) => {
    method = Number(method)
    if (method == 1) {
        return getRepoViaJson()
    } else if (method == 2) {
        return getRepoFromTrending()
    } else if (method == 3) {
        return getRepoFromStarred()
    }
    return []
}

module.exports = { getRepoViaMethod }
