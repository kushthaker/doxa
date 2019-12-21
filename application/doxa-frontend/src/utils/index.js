// helper functions
export function isValidJwt (jwt) {
  if (!jwt || jwt.split('.').length < 3) {
    return false
  }
  const data = JSON.parse(atob(jwt.split('.')[1]))
  const exp = new Date(data.exp * 1000) // JS deals with dates in milliseconds since epoch
  const now = new Date()
  return now < exp
}

export function canAccess(id, _this) {
  var authed = _this.$store.getters.isAuthenticated
  var user = _this.$store.getters.currentUser
  if(authed && user && (user.id == id)) { return true }
  return false
}
