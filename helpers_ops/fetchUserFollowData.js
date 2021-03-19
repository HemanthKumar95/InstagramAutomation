async function getData() {
let username = "gowti_photography"
    try {
        let followers = [], followings = []
        let res = await fetch(`https://www.instagram.com/${username}/?__a=1`)

        res = await res.json()
        let userId = res.graphql.user.id

        let followingsList = []

        let after = null, has_next = true
        while (has_next) {
            await fetch(`https://www.instagram.com/graphql/query/?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables=` + encodeURIComponent(JSON.stringify({
                id: userId,
                include_reel: true,
                fetch_mutual: true,
                first: 50,
                after: after
            }))).then(res => res.json()).then(res => {
                has_next = res.data.user.edge_follow.page_info.has_next_page
                after = res.data.user.edge_follow.page_info.end_cursor
                followings = followings.concat(res.data.user.edge_follow.edges.map(({node}) => {
                    followingsList.push(node.username)
                    return {
                        username: node.username,
                        full_name: node.full_name
                    }
                }))
            })
        }
        // console.log('Followings', followings)

        let followingsElement = document.createElement('TEXTAREA')
        followingsElement.id = 'followingsData'
        followingsElement.innerHTML = followingsList
        document.body.appendChild(followingsElement)

        let followersList = []

        has_next = true
        after = null
        while (has_next) {
            await fetch(`https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables=` + encodeURIComponent(JSON.stringify({
                id: userId,
                include_reel: true,
                fetch_mutual: true,
                first: 50,
                after: after
            }))).then(res => res.json()).then(res => {
                has_next = res.data.user.edge_followed_by.page_info.has_next_page
                after = res.data.user.edge_followed_by.page_info.end_cursor
                followers = followers.concat(res.data.user.edge_followed_by.edges.map(({node}) => {
                    followersList.push(node.username)
                    return {
                        username: node.username,
                        full_name: node.full_name
                    }
                }))
            })
        }
        // console.log('Followers', followers)

        let followersElement = document.createElement('TEXTAREA')
        followersElement.id = 'followersData'
        followersElement.innerHTML = followersList
        document.body.appendChild(followersElement)

    } catch (err) {
        console.log(err)
        console.log('Invalid username')
    }
}

getData()