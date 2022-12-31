const URL = 'https://api.pushshift.io/reddit/search/'

const params = {
    q: 'javascript',
    size: 10,
    subreddit: 'askreddit'

}
let ALL_UTC = []
// Submit First Request....
axios.get(URL + 'comment', {
        params
    })
    .then((response) => {
        // Handle First Response

        let length = response.data.data.length - 1;
        let utc = response.data.data[length].created_utc;
        ALL_UTC.push(utc)
        params.before = utc

        // Make A Second Get Request
        axios.get(URL + 'comment', {
                params
            })
            .then((response) => {

                let length = response.data.data.length - 1;
                let utc = response.data.data[length].created_utc;
                ALL_UTC.push(utc)
                params.before = utc

                // Make A Third Get Request
                axios.get(URL + 'comment', {
                        params
                    })
                    .then((response) => {

                        let length = response.data.data.length - 1;
                        let utc = response.data.data[length].created_utc;
                        ALL_UTC.push(utc)
                        params.before = utc



                        //Make A Fourth Get Request
                        axios.get(URL + 'comment', {
                                params
                            })
                            .then((response) => {

                                let length = response.data.data.length - 1;
                                let utc = response.data.data[length].created_utc;
                                ALL_UTC.push(utc)
                                params.before = utc

                                console.log(`finished all requests... \n${ALL_UTC}`)


                            })


                    })




            })
