<script lang="ts">
  import * as Item from '$lib/components/ui/item/index.js'
  import { getConfig } from './config.remote'
  import { cn } from '$lib/utils'

  const config = await getConfig()
</script>

<div class="h-screen w-screen" style="padding: 100px calc(100vw / 7);">
  <Item.Group class="grid grid-cols-3 gap-4">
    {#each config.links as model (model.name)}
      <div class=" flex h-full w-full flex-wrap items-center justify-center">
        <Item.Root variant="default" class="">
          {#snippet child({ props })}
            <a href={model.url} {...props} class={cn(props.class, 'h-full w-[250px]')}>
              <Item.Header>
                <img
                  src={model.faviconUrl}
                  alt={model.name}
                  width="128"
                  height="128"
                  class="aspect-square w-full rounded-sm object-cover"
                />
              </Item.Header>
              <Item.Content>
                <Item.Title class="text-2xl">{model.name}</Item.Title>
              </Item.Content>
            </a>
          {/snippet}
        </Item.Root>
      </div>
    {/each}
    <a href="http://about:settings">settings</a>
    <!-- Add a website -->
    <!-- Firefox settings -->
  </Item.Group>
</div>
