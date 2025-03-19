/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    return new Promise(async (resolve, reject) => {
        await setTimeout(() => resolve("Done"), millis);
    })
}
