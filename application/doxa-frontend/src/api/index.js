export function fetchUsers() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(users)
    }, 300)
  })
}

const users = [{
  id: 1,
  name: 'callum',
  email: 'maestro@fulfilled.ai'
}]

export function fetchUser(userId) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const user = users.find(user => user.id === userId)
      if(user){
        resolve(user)
      }
      else {
        reject(Error('User does not exist'))
      }
    }, 300)
  })
}

