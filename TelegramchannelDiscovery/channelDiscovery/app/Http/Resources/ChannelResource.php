<?php

namespace App\Http\Resources;

use Illuminate\Http\Resources\Json\JsonResource;

class ChannelResource extends JsonResource
{
    /**
     * Transform the resource into an array.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return array
     */
    public function toArray($request)
    {
        return [
            'id' => $this->id,
            'user_id' => $this->user_id,
            'category_id' => $this->category_id,
            'category' => $this->category->name,
            'imgurl' => $this->photo->path,
            'description' => $this->description,
            'title' => $this->title,
            'members' => $this->members,
            'contact_name' => $this->contact_name,
            'username' => $this->username,
            'contact_address' => $this->contact_address,
            'contact_phone' => $this->contact_phone,
        ];
    }
}
