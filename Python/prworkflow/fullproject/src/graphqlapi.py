
class Queries:

    def __init__(self, owner, name, state,tag=None, countr=30):
        self.name = name
        self.owner = owner
        self.tag = tag
        self.state = state
        self.countr = countr
        print(type(self.countr))
    def pulls(self):
      if self.tag != None :
        query = """
        { repository(name: "%s", owner: "%s") {
              pullRequests(states: %s, last: %i, orderBy: {field: CREATED_AT, direction: ASC},labels:"%s") {
                totalCount
                nodes {
                  title
                  number
                  comments {
                    totalCount
                  }
                  closedAt
                  createdAt
                  labels(last: 10) {
                    nodes {
                      name
                    }
                    totalCount
                  }
                }
              }
            }
          }
      """% ( self.name,self.owner, self.state,self.countr, self.tag)
        return query
      else:
        query = """
        {
          repository(name: "%s", owner: "%s") {
              pullRequests(states: %s, last: %s, orderBy: {field: CREATED_AT, direction: ASC}) {
                totalCount
                nodes {
                  title
                  number
                  comments {
                    totalCount
                  }
                  closedAt
                  createdAt
                  labels(last: 10) {
                    nodes {
                      name
                    }
                    totalCount
                  }
                }
              }
            }
          }
      """% (self.name, self.owner, self.state, self.countr)
        return query