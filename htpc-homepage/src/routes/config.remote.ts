import { query } from '$app/server'
import { file } from 'bun'
import { env } from '$env/dynamic/private'

export const getConfig = query(async () => {
  let config: App.HomepageConfig = {
    links: [],
  }

  try {
    config = await file(env.HOMEPAGE_CONFIG_LOCATION).json()
  } catch (e) {
    console.error(e)
  }

  return config
})
