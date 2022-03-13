const covid19 = require('covid19-stats')
const main = async (inputs, auths, context) => {
  const country = inputs.country
  var stats = await covid19.getCountry(country)
  return stats
}
module.exports.main = main
