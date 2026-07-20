const { Akinator, AkinatorAnswer } = require("./dist")

const run = async () => {
  const api = new Akinator({ region: "en", childMode: false })
  await api.start()
  console.log(`Question: ${api.question}, progress: ${api.progress}`)

  // To answer
  await api.answer(AkinatorAnswer.Yes) // or you can use 0-4
  console.log(`Question: ${api.question}, progress: ${api.progress}`)

  // To check is win or not
  while (!api.isWin) {
    await api.answer(Math.floor(Math.random() * 5)) // random 0-5
    console.log(`Question: ${api.question}, progress: ${api.progress}`)

    // To back last question
    if (Math.floor(Math.random() * 10) + 1 < 4) {
      await api.cancelAnswer()
      console.log(`Question: ${api.question}, progress: ${api.progress}`)
    }
  }

  // if is win
  if (api.isWin) {
    console.log(api.sugestion_name)
    console.log(api.sugestion_desc)
    console.log(api.sugestion_photo)
  }
}

run()