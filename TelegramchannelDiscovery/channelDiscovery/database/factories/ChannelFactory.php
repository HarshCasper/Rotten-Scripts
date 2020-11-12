<?php

/** @var \Illuminate\Database\Eloquent\Factory $factory */

use App\Model;
use Faker\Generator as Faker;

$factory->define(App\Channel::class, function (Faker $faker) {
    return [

        'title'=>$faker->text(50),
        'description'=>$faker->text('50'),
        'members'=>$faker->numberBetween(5,000,700,0000),
        'contact_name'=>$faker->text(30),
        'contact_phone'=>$faker->numberBetween(1,9),
        'contact_address'=>$faker->text(50)

    ];
});
