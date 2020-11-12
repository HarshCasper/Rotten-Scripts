<?php

use Illuminate\Database\Seeder;

class ChannelTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        factory(App\Channel::class,30)->create([
            'user_id'=>$this->getRandomUserId(),
            'photo_id'=>$this->getRandomPhotoId(),
            'category_id'=>$this->getRandomCategoryId()
        ]);
    }
    private function getRandomUserId(){
        $user = \App\User::inRandomOrder()->first();
        return $user->id;
    }

    private function getRandomPhotoId(){
        $photo = \App\Photo::inRandomOrder()->first();
        return $photo->id;
    }

    private function getRandomCategoryId(){
        $category = \App\Category::inRandomOrder()->first();
        return $category->id;
    }
}
